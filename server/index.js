const fetch = (...args) => import('node-fetch').then(({default: fetch}) => fetch(...args));
require('dotenv').config();
const express = require('express')
var UAParser = require('ua-parser-js');
const {v1: uuidv1, v4: uuidv4} = require('uuid');

const app = express()
const port = 80

const mongoose = require('mongoose');
const bodyParser = require('body-parser');

// ENTER YOUR MONGO CLUSTER URI HERE
const uri = 'mongodb://localhost:27017/'

// for mongo
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));

//connnects to mongoDb
mongoose.connect(uri, { useNewUrlParser: true });

// /schema for the mongo json
const notesSchema = {
  title: String,
  dateTime: String,
  uuid: String,
  counter: Number,
  stats: String
}

//assigns schema to mongodb
const Note = mongoose.model('email-tracker', notesSchema);
// Note.remove({}).exec()    //  removes all past data on reload

// used to serve file
app.use(express.static(__dirname))

app.post('/', (req, res) => {
  async function main() {
    var dtResponse = await fetch('http://worldtimeapi.org/api/timezone/Etc/UTC');
    var dtData = await dtResponse.json();

    var dateTime = dtData.datetime.split("T")[0] + " " + dtData.datetime.split("T")[1].split(".")[0] + ' UTC'
    var uuid = uuidv4()
    var newNote = new Note({
      title: req.body.title,
      dateTime: dateTime,
      uuid: uuid,
      counter: 0,
      stats: 'Null'
    });
    newNote.save();

    res.json({ uuid: `p?uuid=${uuid}` });
  }
  main()
})

// http://yourURL.com/p?uuid=
app.get('/p', function(req, res) {
  async function main() {
    var uuidParam = req.query.uuid
    var uuidParamChecker = /^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$/.test(uuidParam)
    
    var dtResponse = await fetch('http://worldtimeapi.org/api/timezone/Etc/UTC');
    var dtData = await dtResponse.json();
    var dateTime = dtData.datetime.split("T")[0] + " " + dtData.datetime.split("T")[1].split(".")[0] + ' UTC'

    var ip = await fetch(`http://ip-api.com/json/${req.headers['x-forwarded-for']}`);
    var location = await ip.json()

    var infoJson =  {
      time: dateTime,
      ip: location.query,
      country: location.country,
      regionName: location.regionName,
      city: location.city,
      zip: location.zip,
      lat: location.lat.toString(),
      lon: location.lon.toString(),
      isp: location.isp,
      org: location.org,
      as: location.as
    }

    if (uuidParamChecker === true) {
      Note.find({uuid: uuidParam}, async function(err, notes) {
        if (notes.length === 0) {
          res.send("uuid not active");
        } else {

          var doc = await Note.findOne({uuid: uuidParam});
          // checks if the link is being clicked for the first time
          if (doc.stats == 'Null'){
            var main = await JSON.stringify(infoJson)
            // console.log(main);
            await Note.findOneAndUpdate({ uuid: uuidParam }, { stats: '[' + main.toString() + ']' });
          } else {    // if not it appends a json with the latest click data
            
            var oldArrs = await doc.stats.toString()
            var docStats = await doc.stats
            var arr = []
            var i = 0
            while (i != JSON.parse(doc.stats).length) {
              arr.push(JSON.parse(doc.stats)[i])
              i++
            }
            arr.push(infoJson)
            let final = JSON.stringify(arr)

            await Note.findOneAndUpdate({ uuid: uuidParam }, { stats: final.toString() });
          }

          Note.findOneAndUpdate({uuid: uuidParam}, {$inc : {'counter' : 1}}).exec();
          res.sendFile(__dirname + '/img.png');
        }
      })
    } else {
      res.send("please enter a valid uuid");
    }

  }
  main()
});

app.get('/data', function(req, res) {
  Note.find({}, async function(err, notes) {
    res.send(notes)
  })
});

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})

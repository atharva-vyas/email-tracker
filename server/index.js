const fetch = (...args) => import('node-fetch').then(({default: fetch}) => fetch(...args));
require('dotenv').config();
const express = require('express')
var UAParser = require('ua-parser-js');
const {v1: uuidv1, v4: uuidv4} = require('uuid');

const app = express()
const port = 3000

const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const uri = process.env.MONGO_URI
// const fetch = require('node-fetch');

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
  counter: Number
}

//assigns schema to mongodb
const Note = mongoose.model('note', notesSchema);
Note.remove({}).exec()    //  removes all past data on reload

// used to serve file
app.use(express.static(__dirname))

app.post('/', (req, res) => {
  async function dt() {
    const dtResponse = await fetch('http://worldtimeapi.org/api/timezone/Etc/UTC');
    const dtData = await dtResponse.json();

    let dateTime = dtData.datetime.split("T")[0] + " " + dtData.datetime.split("T")[1].split(".")[0] + ' UTC'

    let uuid = uuidv4()
    let newNote = new Note({
      title: req.body.title,
      dateTime: dateTime,
      uuid: uuid,
      counter: 0
    });
    newNote.save();

    res.json({ uuid: `/p?uuid=${uuid}` });
  }
  dt()
})

// http://localhost:3000/p?uuid=
app.get('/p', function(req, res) {
  let uuidParam = req.query.uuid
  let uuidParamChecker = /^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$/.test(uuidParam)
  if (uuidParamChecker === true) {
    Note.find({uuid: uuidParam}, async function(err, notes) {
      if (notes.length === 0) {
        res.send("uuid not active");
      } else {
        Note.findOneAndUpdate({uuid: uuidParam}, {$inc : {'counter' : 1}}).exec();
        res.sendFile(__dirname + '/img.png');
      }
    })
  } else {
    res.send("please enter a valid uuid");
  }
});

app.get('/data', function(req, res) {
  Note.find({}, async function(err, notes) {
    res.send(notes)
  })
});

// app.use('/arr', express.static(__dirname))

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})

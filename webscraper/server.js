const express = require('express')
const app = express()
const port = process.env.PORT || 3030
var bodyParser = require('body-parser')
const {MongoClient} = require("mongodb");

const accountSid = process.env.accountSid;
const authToken = process.env.authToken;
const twilio = require("twilio")(accountSid, authToken);
const uri = process.env.RentProjectMongo
const client = new MongoClient(uri);
const db = client.db("main")
const col = db.collection("Properties")
app.use(express.static('public'))
app.use(bodyParser.urlencoded({extended:true}))
app.post("/apartment", async (req, res) => {
    console.log(req.body)
    const obj = {
        type: req.body.type,
        cost_low: parseInt(req.body.priceLow),
        cost_high: parseInt(req.body.priceHigh),
        location: {
            line1: req.body.line1,
            city: req.body.city
        },
        bedrooms: parseInt(req.body.bedrooms),
        bathrooms: parseInt(req.body.bathrooms),
        sqft: parseInt(req.body.sqft),
    }
    console.log(obj)
    await col.insertOne(obj)
    res.send(200)
    // TODO get user's phone
    twilio.messages
        .create({ body: "New listed has been posted on R4R! Check it out on our site.", from: "+16206596194", to: process.env.DemoPhoneNumber })
        .then(message => console.log(message.sid));
})


app.listen(port, () => {
    console.log(`Example app listening on port ${port}`)
})



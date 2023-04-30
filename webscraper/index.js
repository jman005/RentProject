const puppeteer = require('puppeteer')
const {MongoClient} = require("mongodb");
// Replace the uri string with your connection string.
const uri = process.env.RentProjectMongo
const client = new MongoClient(uri);

async function tutorial(num) {
    try {
        // Specify the URL of the dev.to tags web page
        const URL = "https://rentals.ca/mississauga?p=" + num;

        // Launch the headless browser
        const browser = await puppeteer.launch();
        const page = await browser.newPage();
        // Go to the webpage
        await page.goto(URL);

        // Perform a function within the given webpage context
        const data = await page.evaluate(async () => {
            const results = JSON.parse(JSON.stringify(window.App.store.search.response.data.listings))
            return results.map(x => ({
                "type": 1,
                "cost_low": x.rent_range[0],
                "cost_high": x.rent_range[1] ?? x.rent_range[0],
                "location": {
                    "longitude": x.location.lng,
                    "latitude": x.location.lat,
                    "line1": x.address1,
                    "postal": x.postal_code,
                    "city": x.city.name,
                    "province": "Ontario",
                    "line2": x.address2
                },
                "coordinates": {type: "Point", coordinates: [x.location.lng, x.location.lat]},
                "bedrooms": x.beds_range[1] ? Math.round((x.beds_range[0] + x.beds_range[1]) / 2) : x.beds_range[0],
                "bathrooms": x.baths_range[1] ? Math.round((x.baths_range[0] + x.baths_range[1]) / 2) : x.baths_range[0],
                "sqft": x.dimensions_range[1] ? Math.round((x.dimensions_range[0] + x.dimensions_range[1]) / 2) : x.dimensions_range[0],
                "accessible": null,
                "roommates": null,
                "coed": null,
                "gender_restricted": null,
                "images": x.photos.map(y => y.url)
            }))
        });

        // Print the result and close the browser
        await browser.close();
        console.log(data)
        return data
    } catch (error) {
        console.error(error);
    }

}


for (let i = 1; i <= 10; i++) {
    tutorial(i).then(async x => {
        const db = client.db("main")
        const col = db.collection("Properties")
        await col.insertMany(x)
    }).then(() => console.log("Done!"))
}

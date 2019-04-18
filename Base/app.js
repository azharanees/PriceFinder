const express = require('express');
const app = express();
let eBay = require('ebay-node-api');


let ebay = new eBay({
    clientID: "pricefin-pricefin-PRD-bf2cd4cf7-bca5e5ee",
    limit: 10, // fetches top 10 results in form of JSON.
    env: "PRODUCTION" // optional default = "PRODUCTION"
})

const searchTerm = "iphone 5";
var jsonRes =[];
 stri = "";
 
var prices = 0;
var pArr = [];
var total  = 0;
ebay.findItemsByKeywords(searchTerm).then((data) => {
    jsonRes = data;
    for(var searchResult in jsonRes[0].searchResult[0].item){
        
        prices = (JSON.stringify(jsonRes[0].searchResult[0].item[searchResult].sellingStatus[0].currentPrice[0].__value__));
              var x = "123.23";

        var fPrice = parseFloat(prices.replace(/"/g,''));
        console.log((fPrice));
        total =fPrice+total;
        pArr.push(fPrice);


    }

   console.log("Total : " +total);
   console.log("Average : " +total/10);

    stri = JSON.stringify(jsonRes);

    for (const item in data) {
        if (data.hasOwnProperty(item)) {
            const element = data[item];
            
        }
    }


}, (error) => {
    console.log(error);
});





app.use((req,res,next) => {
res.status(200).json({
    message: "It works!",  
    Total : total,
    Average :total/10,
    });
});


module.exports = app;
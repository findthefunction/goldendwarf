d3.json("items.json").then((data) => {
    // console.log(data)
    var tbody = d3.select("tbody")
    data.forEach(function(x)
    {
        // console.log(x)
        var row = tbody.append("tr")
        Object.entries(x).forEach(function([key,value]){
           
           var cell =  row.append("td")
           cell.text(value)




        })
    })
})
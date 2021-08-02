d3.json("/data").then((data) => {
    // console.log(data)
    // var tbody = d3.select("tbody")
    // data.forEach(function(x)
    // {
    //     // console.log(x)
    //     var row = tbody.append("tr")
    //     Object.entries(x).forEach(function([key,value]){
    //        var cell =  row.append("td")
    //        cell.text(value)
    //     })
    // })

    console.log(data);
})

 // 4. Create the trace for the gauge chart.

// 5. Create the layout for the gauge chart.
var gaugeLayout = { 
     width: 500, 
     height: 500, 
     font: { color: "black", family: "Arial" }

};


var data = [
    {
      domain: { x: [0, 1], y: [0, 1] },
      value: 450,
      title: { text: "Speed" },
      type: "indicator",
      mode: "gauge+number",
      delta: { reference: 400 },
      gauge: { axis: { range: [null, 500] } }
    }
  ];
  
  var layout = { width: 600, height: 400 };
  Plotly.newPlot('gauge', data, layout);

// 6. Use Plotly to plot the gauge data and layout.
// Plotly.newPlot('gauge', gaugeData, gaugeLayout, { responsive: true }); 
// Line_Chart 
var trace1 = {
  x: [1, 2, 3, 4],
  y: [10, 15, 13, 17],
  type: 'line'
};

var trace2 = {
  x: [1, 2, 3, 4],
  y: [16, 5, 11, 9],
  type: 'line'
};

var data = [trace1, trace2];

Plotly.newPlot('line', data);
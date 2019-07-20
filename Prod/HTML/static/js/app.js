function buildPlot() {
  /* data route */
var url = "/crank";
d3.json(url).then(function(response) {

  console.log(response);

  var data = [response];

  var layout = {
    title: "City Ranks",
    xaxis: {
      title: "City"
    },
    yaxis: {
      title: " - Worst---------Best +"
    }    
  };

  Plotly.newPlot("plot", data, layout);
});
}
buildPlot();

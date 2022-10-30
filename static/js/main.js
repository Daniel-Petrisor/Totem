
// const ctx = document.getElementById('myChart').getContext('2d');

// var graphData = {
//     type: 'line',
//     data: {
//         labels: ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'],
//         datasets: [{
//             label: 'Temperatura',
//             data: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
//             backgroundColor: [
//                 'rgba(255, 99, 132, 0.5)',
//             ],
           
//             borderWidth: 2
//         }]
//     },
//     options: {
//         scales: {
//             y: {
//                 beginAtZero: true
//             }
//         }
//     }
// }

// const myChart = new Chart(ctx, graphData);


// var socket = new WebSocket('ws://127.0.0.1:8000/ws/graph/');

// socket.onmessage = function(e){
//     var djangoData = JSON.parse(e.data);
//     //document.querySelector('#app').innerText = djangoData.value;
//     console.log(djangoData);

//     var newGraphData = graphData.data.datasets[0].data;
//     newGraphData.shift();
//     newGraphData.push(djangoData.value);

//     graphData.data.datasets[0].data = newGraphData;
//     myChart.update();

    
// }
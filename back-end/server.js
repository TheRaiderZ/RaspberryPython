const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const app = express();
const port = 8000;

app.use(bodyParser.json());
app.use(cors());
app.use(express.urlencoded({ extended: true }));


data = {
  "Datas": [
  {
    "rotationG": "-28",
    "rotationR": "-12"
  },
  {
    "distance": "20",
  }
]
}



//routes 

// a = app.post("/postDatas", (req, res) => {});
// console.log(a);
// app.get('/getDatas', (req, res) => {
//   res.send(data,a)
// });




// listen on the port
app.listen(port);
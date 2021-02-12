'use strict';

const fs = require('fs');

(function() {
  try {
    let rawdata = fs.readFileSync('select_list_data.json');
    let student = JSON.parse(rawdata);
    console.log(student);
    alert(student);
    document.getElementById("json").innerHTML = student;
  } catch (err) {
    document.getElementById("json").innerHTML = "student";
    alert("Nope!");
  }
}());

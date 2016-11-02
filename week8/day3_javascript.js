console.log("Getting started with javascript");

var myNumber = 10 / 90.23;
console.log(myNumber);

myArray = [10, "fool", [19, 90, 23], "why"]
console.log(myArray);
console.log(myArray[2]);
console.log(myArray[2][1]);


for (var i = 0 ; i < myArray.length ; i++ ) {
    var item = myArray[i];
    console.log(item);
}

var myObject = {
  "myName": "joel",
  "myAge": 33
};

console.log(myObject["myName"]);
console.log(myObject.myName);


console.log(myFunc(9, 10)

var myFunc =  function(x, y) {
  return x * y;
};

console.log(myFunc(p, 4));

var sillyArray = [9, 34, 123, 12, 4, 52];

var loopFunc = function(item) {
  console.log(item);
};

silltArray.forEach(loopFunc);

sillyArray.forEach(function(item)){
  console.log(item);
}

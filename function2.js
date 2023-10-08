//Function Statement

function xyz(){
    console.log("Hello");
}

//Function Expression

var a = function(){
    console.log("hello");
}

//Anonymous function
var b = function(){
    console.log("Anonymous function");
}

//Named function
var a = function xyz(){
    console.log("Named Function");
}

//First class function
var b = function(param){
    return function xyz(){
        console.log("ABC");
    }
}

//Callback function
function x(y){

}
x(function y(){
  // function y is callbaack function- passed as an argument to another function
});

//Example with setTimeout

setTimeout(function(){
    console.log("timer");
},5000);
function x(y){           //x() is higher order function- take another function as an argument
    console.log("x");
    y();
}
x(function y(){          //y() is callback function
    console.log("y");    //o/p: x,y,timer
});


//eventListener with callback function
document.getElementById("clickMe").addEventListener("click",function xyz(){ //xyz() callback function
    console.log("button clicked");
});

//how many time button got clicked or closure with eventListener
function attachEventListener(){
    let count = 0;
    document.getElementById("clickMe").addEventListener("click",function xyz(){ //xyz() callback function
        console.log("button clicked");
        ++count;
    });
}
attachEventListener();

//web APIs
setTimeout();
fetch();
//DOM APIs, local storage, console, location etc.
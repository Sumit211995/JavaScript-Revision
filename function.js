/*Normal Function*/
function printHeart(){
    console.log("<3");
}
printHeart();

function rant(message){
    console.log(`${message.toUpperCase()}`);
    console.log(`${message.toUpperCase()}`);
    console.log(`${message.toUpperCase()}`);
}
rant("I hate beets");

/*function with arguments*/
function isSnakeEyes(dice1, dice2){
    if(dice1 === 1 && dice2 === 1){
        console.log("Snake Eyes!");
    }else{
        console.log("Not Snake Eyes!");
    }
}
isSnakeEyes(1,1);
isSnakeEyes(2,5);

/*Weather*/
function isShortsWeather(temp){
    if(temp >=75){
        return true;
    }else{
        return false;
    }
}
isShortsWeather(80);
isShortsWeather(48); 

/*Find last Element in array*/
function lastElement(arr){
    let arrayLength =arr.length;
    if(arrayLength >= 1){
        return arr[arrayLength-1];
    }else{
        return null;
    }
}
lastElement([3,5,7]);
lastElement([1]);
lastElement([]);

/*Capitalize exercise*/
function capitalize(str){
    let firstLetter = str[0]
    let capitalize = firstLetter.toUpperCase();
    let remainingStr = str.slice(1);
    return capitalize.concat(remainingStr);
}
capitalize("eggplant");

/*Sum of array*/
function sumArray(arr){
    let sum=0;
    for(let x of arr){
        sum = sum + x;
    }
    return sum;
}
sumArray([1,2,3]);
sumArray([2,2,2,2]);
sumArray([50,50,1]);

/*Days of the week*/
function returnDay(num){
    let arr = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
    if(num < 1 || num >7){
        return null;
    }else{
        return arr[num-1]
    }
}
returnDay(1);
returnDay(7); 
returnDay(4);
returnDay(0);

/*Hoisting- From anywhere we can access the function 
            without any error even we have initialize it*/

getName();

function getName(){
    console.log("function invoked");
}

/*Example*/
var x=1;
a();
b();
console.log(x);
function a(){
     var x=10;
     console.log(x);
}

function b(){
    var x=100;
    console.log(x);
}
//Output: 10, 100, 1


/*window-global object*/
var a = 10;
function b(){
    var x = 10;
}
console.log(window.a); //global space
console.log(a);
console.log(this.a);  //point to window object

/*Scope*/
function a(){           //a() is lexically inside a global scope.
    var b = 10;
    c();
    function c(){
        console.log(b); //10   the finction c() is lexically inside a() function.
    }
}
a();
console.log(b); //b is not defined
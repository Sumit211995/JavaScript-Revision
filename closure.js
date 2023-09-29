//let a = 10;
//let a = 20; Syntax error, cannot redeclare in same scope

//var b = 10;
//var b = 100; no error

/*Error*/

//typeError
// const b = 10; //Assignment to constant variable
// b = 100;

//Syntax Error
// const b; //declaration must be initialize

//ReferenceError
// console.log(a); //cannot access 'a' before initialization
// let a = 1900;

/*Closure*/ //function with it's lexical scope known as closure
//ex-01
function x(){           //closure: x
    var a = 7;
    function y(){
        console.log(a);
    }
    y();
}
x();

//ex-02
function x(){
    var a = 9;
    function y(){
        console.log(a);
    }
    return y;
}
var z = x();
console.log(z); //function y
z(); //output 7


//ex-03
function x(){
    var a = 9;
    function y(){
        console.log(a);
    }
    a = 100;
    return y;
}
var z = x();
console.log(z); //function y
z(); //output 100

//ex-03
function z(){        //  closure:z
    var b = 900;
    function x(){     // closure:x
        var a = 7;
        function y(){
            console.log(a,b); //7, 900
        }
        y();
    }
    x();
}
z();

//setTimeOut
//ex-1
function x(){
    var i = 1;
    setTimeout(function(){
        console.log(i);    //print 1 after 1 sec
    },1000);
}
x();

//ex-2
function x(){   //closure x
    var i = 1;
    setTimeout(function(){
        console.log(i);
    }, 3000);
    console.log("hello");    // o/p: hello and after 3 sec it will print 1
}
x();

//ex-03
function x(){    //closure x
    for(var i = 1; i<=5; i++){
        setTimeout(function(){
            console.log(i);  //i=6
        }, i*1000);
    }                    // o/p: hello then it will print 6,6,6... six times after every 1 sec
     console.log("hello");                               
}     //js don't wait for timeout funtion 
x();      //  and loop is continue running and because of var, i refer to same memory location.

//ex-04
function x(){    //closure x
    for(let i = 1; i<=5; i++){
        setTimeout(function(){
            console.log(i);  
        }, i*1000);
    }                    // o/p: hello then it will print 1,2,3..6 after every 1 sec
     console.log("hello");                               
}     
x();  //let has block scope, that means for each iteration this i is a new variable altogether

//ex-05 another way with var
function x(){
    for(var i = 1; i<=5; i++){
        function close(x){
            setTimeout(function(){
                console.log(i);
            },i*1000);
        }
        close(i);
    }
    console.log("hello");
}
x();

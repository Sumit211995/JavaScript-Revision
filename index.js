// var character = prompt("Enter Your Message:");
// var charCount = character.length;
// alert("you have written " + charCount + " character and you have " + (200-charCount) + " remaining character!");

/*BMI Calculator*/
// function bmiCalculator(weight, height){
//     var bmi = weight / Math.pow(height,2);
//     return bmi;
// }
// var bmi = bmiCalculator(70,1.78);
// console.log(bmi);

/*Love Calculator with random number generator*/

// prompt("what is your name? ");
// prompt("what is their name? ");

// var loveScore = Math.random() * 100;
// loveScore = Math.floor(loveScore) +1;
// alert("your love score is " + loveScore);
// console.log(loveScore);

/*Leap year*/

// function leapYear(year){
//     if(year % 4 === 0){
//         if(year % 100 === 0){
//             if(year % 400 === 0){
//                 return "leap year";
//             }else{
//                 return "not a leap year";
//             }
//         }else{
//             return "leap year";
//         }
//     }else{
//         return "not a leap year";
//     }
// }

// var leap = leapYear(2000);
// console.log(leap);

/*Print FizzBuzz*/
// var count;
// var output = [];
// function fizzBuzz(){
//     for(count=1; count<=100; count++){
//         if(count % 3 === 0 && count % 5 === 0){
//             output.push("FizzBuzz");
//         }else if(count % 3 === 0){
//             output.push("Fizz");
//         }else if(count % 5 === 0){
//             output.push("Buzz");
//         }else{
//             output.push(count);
//         }
//     }
//     console.log(output);
// }
// fizzBuzz();

/*WhosPaying*/
function whosPaying(names){
    var noOfPerson = names.length;
    var randomPersonPosition = Math.floor(Math.random()*noOfPerson);
    var randomPerson = names[randomPersonPosition];
    return randomPerson + " is going to buy dinner today!";
}

var names = ["ABC", "XYZ", "JKL", "MNO", "STU"];
randomPerson = whosPaying(names);
console.log(randomPerson);
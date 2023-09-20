var names = ["ABC", "XYZ", "JKL", "MNO"];

console.log(names);
//push()- add the element at the end of the array
names.push("PQR");
names.push("STU");
console.log(names);

//pop()- remove element from the end
names.pop();
console.log(names);
//unshift()- add the element at the front
names.unshift("KIT");
names.unshift("FIT");
console.log(names);

//shift()- remove element from the front
names.shift();
console.log(names);

//concat()- concat two array but not change original array
var nums = [1,2,3];
var newArray = nums.concat(names);
console.log(newArray);
console.log(nums);

//indexOf()- provide position of element
var position = names.indexOf("JKL");
console.log(position);

//reverse()- reverse all element and change original array
nums.reverse();
console.log(nums);

//for loop
const people = ["Scooby", "Velma", "Daphne", "Shaggy", "Fred"];

for(let i=0; i<people.length; i++){
    console.log(people[i].toUpperCase());
}
 //for of loop
const numbers = [1,2,3,4,5,6,7,8,9];
for(let x of numbers){
    x = x*x;
    console.log(x);
 }

//for in loop for object
const details = {
    firstName: "XYZ",
    lastName: "ABC",
    age: 25,
    job: "Developer",
    friends: ["JKL", "MNO", "TUV"]
};
for(let info in details){ 
    console.log(info); //info stores only key data not value
    console.log(`${info} : ${details[info]}`); //if we want to print all (key with value)
}

/*Object is used to store various keyed collections and more complex entities.*/

//Creating Object
const details = {
    firstName: "XYZ",
    lastName: "ABC",
    age: 25,
    job: "Developer",
    friends: ["JKL", "MNO", "TUV"]
};
//Accessing object value using (.) dot operator
console.log(details.age);

//Accessing object value using ([]) bracket
console.log(details["job"]);



//We also can include array, function, object etc. inside object in the form of key-value pairs.
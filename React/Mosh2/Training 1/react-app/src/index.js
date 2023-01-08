import React from "react";
import ReactDOM from "react-dom";

const element = <h1>Hello World</h1>;
ReactDOM.render(element, document.getElementById("root"));

const colors = ["red", "green", "blue"];
const list = colors.map((color) => `<li>${color}</li>`);
console.log(list);

const address = {
  street: "",
  city: "",
  country: "",
};

const { street: st, city, country } = address;

class Person {
  constructor(name) {
    this.name = name;
  }

  walk() {
    console.log("Walk");
  }
}
class Teacher extends Person {
  constructor(name, degree) {
    super(name);
    this.degree = degree;
  }
  teach() {
    console.log("Teach");
  }
}

const teacher = new Teacher("Mahdi", "MSc");
console.log(teacher);

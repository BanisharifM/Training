// Code goes here!
type Admin = {
  name: string;
  privileges: string[];
};
type Employee = {
  name: string;
  startDate: Date;
};
type ElevatedEmployee = Admin & Employee;
const e1: ElevatedEmployee = {
  name: "mahdi",
  privileges: ["a", "b"],
  startDate: new Date(),
};
type UnknownEmployee = Employee | Admin;
function printEmployeeInformation(emp: UnknownEmployee) {
  console.log("Name: " + emp.name);
  if ("privileges" in emp) {
    console.log("Privileges: " + emp.privileges);
  }
  if ("startDate" in emp) {
    console.log("Privileges: " + emp.startDate);
  }
}
printEmployeeInformation(e1);
printEmployeeInformation({ name: "Ali", startDate: new Date() });

// const userInput = <HTMLInputElement>document.getElementById("user-input")!;
const userInput = document.getElementById("user-input")! as HTMLInputElement;
userInput.value = "hi there";

interface ErrorContainer {
  [prop:string]:string;
}
const errorBag:ErrorContainer={
  email:"not a valid email",
  userName:"must start with a capital character"
};
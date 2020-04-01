console.log("compiling...");
class Person {
    readonly id:number;
    name:string;
    constructor(id:number,name:string) {
        this.id=id;
        this.name=name
    }
}
class Teacher extends Person{
    constructor(id:number,name:string) {
        super(id,name);
    }
}
let teacher=new Teacher(1,"ali");
console.log(teacher.id);

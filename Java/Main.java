public class Main{
  public static void main(String[] args){
    System.out.println("Hello World");
    int x=3,y=10;
    int sum=x+y;
    System.out.println(sum);
    int randNum=(int)(Math.random()*101);
    System.out.println(randNum);
    System.out.println((x>10) ? 20 :  15);
    // while(x<10){
    //   System.out.println(x++);
    // }
    myMethod("Mahdi");
  }

  static void myMethod(String input){
    System.out.println("Your input is: "+input);
  }
}
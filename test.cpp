int main = 0 ;
string a = "String Constant"
void setup() {
  Serial.begin (9600) ;
}
// Only Comment Line
void loop(){
  if(main>=100) { // Additional Comment Line
    main=0;
  }
  Serial.println(main);
  main += 1 ;
}


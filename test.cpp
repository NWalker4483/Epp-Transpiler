int main = 0 ;
void setup() {
  Serial.begin (9600) ;
}

void loop(){
  if(main>=100) {
    main=0;
  }
  Serial.println(main);
  main += 1 ;
}


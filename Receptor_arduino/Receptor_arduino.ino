int led = 13;
char dato;

void setup() {
  // put your setup code here, to run once:
  pinMode(13, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){
    dato = Serial.read();

    if(dato == '1'){
      digitalWrite(13, HIGH);
      Serial.print("Encendido \n");
    }
    if(dato == '2'){
      digitalWrite(13, LOW);
      Serial.print("Apagado \n");
    }
  }
}

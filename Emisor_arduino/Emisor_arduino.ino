int pin = A5;
int valor;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(pin, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  valor = analogRead(pin);
  Serial.print(valor);
  delay(100);
}

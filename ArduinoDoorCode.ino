// Include the AccelStepper Library
#include <AccelStepper.h>

// define step constant
#define FULLSTEP 4
#define STEP_PER_REVOLUTION 2048 // this value is from datasheet

// Pins entered in sequence IN1-IN3-IN2-IN4 for proper step sequence
AccelStepper stepper(FULLSTEP, 11, 9, 10, 8);

void setup() {
  Serial.begin(9600);
  stepper.setMaxSpeed(200.0);   // set the maximum speed
  stepper.setAcceleration(200.0); // set acceleration
  pinMode(2, INPUT);
  pinMode(4, INPUT);
  pinMode(12, INPUT);
  pinMode(13, OUTPUT);
  stepper.setSpeed(200);         // set initial speed
  stepper.setCurrentPosition(0); // set position
  // stepper.moveTo(STEP_PER_REVOLUTION); // set target position: 64 steps <=> one revolution
}

void loop() {
  if(Serial.available()){
    String command = Serial.readStringUntil('\n');
    // change direction once the motor reaches target position
    if(digitalRead(4) == HIGH && command != "ON"){ // hand sign & allow people
      digitalWrite(7, HIGH);
      digitalWrite(13, LOW);
      Serial.println("Allowing People In...");
      stepper.moveTo(1000);
    }
    else if(command == "ON"){ // redlight
      digitalWrite(13, HIGH);
      digitalWrite(7, LOW);
      stepper.moveTo(-1000);
    }
    else if(digitalRead(4) == LOW){
      digitalWrite(7, LOW);
      digitalWrite(13, LOW);
    }
  }

}

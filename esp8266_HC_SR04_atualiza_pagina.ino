#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>

#define AP_SSID "EACI_ESP8266"
#define AP_PASSWORD "senha123"
#define WEB_PORT 80
#define TRIGGER_PIN 5
#define ECHO_PIN 4

ESP8266WebServer server(80);

// Set your Static IP address
IPAddress local_IP(192, 168, 4, 1);
// Set your Gateway IP address
IPAddress gateway(192, 168, 1, 1);
IPAddress subnet(255, 255, 0, 0);



void setup() {
  Serial.begin(9600);
  pinMode(TRIGGER_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  WiFi.softAP(AP_SSID, AP_PASSWORD);
  IPAddress ip = WiFi.softAPIP();
  Serial.print("AP IP address: ");
  Serial.println(ip);
  server.on("/", HTTP_GET, handleRequest);
  server.on("/update", HTTP_GET, handleUpdate);
  server.begin(WEB_PORT);
}

void loop() {
  server.handleClient();
}

void handleUpdate() {
  long distance = measureDistance();
  server.send(200, "text/plain", String(distance));
}

void handleRequest() {
  String response = "<html>";
  response += "<head><title>Medição de Distância</title></head>";
  response += "<body>";
  response += "<meta charset='UTF-8'>";
  response += "<style>";
  response += "body { text-align: center;} h1 { font-size: 40px;font-family: Arial, sans-serif;} p { font-size: 40px;font-family: Arial, sans-serif;}";
  response += "</style>";
  response += "<h1>Medição de Distância</h1>";
  response += "<p>Distância: <span id='distance'></span> mm</p>";
  response += "<script>";
  response += "setInterval(function() {";
  response += "var xhttp = new XMLHttpRequest();";
  response += "xhttp.onreadystatechange = function() {";
  response += "if (this.readyState == 4 && this.status == 200) {";
  response += "document.getElementById('distance').innerHTML = this.responseText;";
  response += "}";
  response += "};";
  response += "xhttp.open('GET', '/update', true);";
  response += "xhttp.send();";
  response += "}, 1000);";
  response += "</script>";
  response += "</body></html>";
  server.send(200, "text/html", response);
}

long measureDistance() {
  digitalWrite(TRIGGER_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIGGER_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIGGER_PIN, LOW);
  long duration = pulseIn(ECHO_PIN, HIGH);
  long distance = duration * 0.034 / 2 * 10;
  return distance;
}

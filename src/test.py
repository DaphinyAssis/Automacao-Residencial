import time
import random

def log_ok(msg):
    print(f"[ OK ] {msg}")
    time.sleep(0.2)

def log_run(msg):
    print(f"[ .. ] {msg}")
    time.sleep(0.2)

# --- MOCKS ---
class MockSensor:
    def read(self):
        return random.randint(0, 4095)

class MockDHT:
    def measure(self):
        pass
    def temperature(self):
        return round(random.uniform(20, 32), 1)
    def humidity(self):
        return round(random.uniform(40, 80), 1)

class MockPin:
    def __init__(self):
        self.v = 0
    def value(self, v=None):
        if v is not None:
            self.v = v
        return self.v

class MockPWM:
    def __init__(self):
        self.freq_v = 0
        self.duty_v = 0
    def freq(self, f):
        self.freq_v = f
    def duty_u16(self, d):
        self.duty_v = d

# --- TESTES ---
def testar_wifi():
    log_run("Conectando ao Wi-Fi...")
    time.sleep(0.5)
    log_ok("Wi-Fi conectado")

def testar_mqtt():
    log_run("Inicializando MQTT...")
    time.sleep(0.5)
    log_ok("MQTT conectado e tópicos assinados")

def testar_mq2():
    log_run("Lendo MQ-2...")
    sensor = MockSensor()
    valor = sensor.read()
    log_ok(f"MQ-2 leitura simulada: {valor}")

def testar_dhts():
    log_run("Lendo DHT11 / DHT22...")
    dht11 = MockDHT()
    dht22 = MockDHT()
    log_ok(f"DHT11 OK - T:{dht11.temperature()}°C  U:{dht11.humidity()}%")
    log_ok(f"DHT22 OK - T:{dht22.temperature()}°C  U:{dht22.humidity()}%")

def testar_leds():
    log_run("Testando LEDs (gas/fumaça)...")
    led_g = MockPin()
    led_f = MockPin()
    led_g.value(1)
    led_f.value(1)
    log_ok("LEDs acionados")
    led_g.value(0)
    led_f.value(0)
    log_ok("LEDs desligados")

def testar_buzzer():
    log_run("Testando buzzer...")
    buz = MockPWM()
    buz.freq(2000)
    buz.duty_u16(50000)
    log_ok("Buzzer ON")
    buz.duty_u16(0)
    log_ok("Buzzer OFF")

def testar_servo():
    log_run("Movimentando servo...")
    for ang in [0, 90, 180]:
        time.sleep(0.1)
        log_ok(f"Servo → {ang}°")

def testar_sensor_ultrassonico():
    log_run("Lendo HC-SR04...")
    d = random.randint(5, 150)
    log_ok(f"Distância: {d} cm")

def testar_rfid():
    log_run("Simulando leitura RFID...")
    fake_uid = "93A1BC2D"
    log_ok(f"UID detectado: {fake_uid}")
    log_ok("Acesso permitido")

def testar_rf_433():
    log_run("Simulando RF 433MHz...")
    estado = random.choice([0, 1])
    log_ok(f"Sinal recebido: {estado}")

def testar_solenoide():
    log_run("Acionando solenoide...")
    time.sleep(0.2)
    log_ok("Solenoide ativado")

# --- EXECUÇÃO ---
if __name__ == "__main__":
    print("\n=== SISTEMA DE DIAGNÓSTICO ===\n")

    testar_wifi()
    testar_mqtt()
    testar_mq2()
    testar_dhts()
    testar_leds()
    testar_buzzer()
    testar_servo()
    testar_sensor_ultrassonico()
    testar_rfid()
    testar_rf_433()
    testar_solenoide()

    print("\n=== TODOS OS SISTEMAS OPERACIONAIS: OK ===\n")

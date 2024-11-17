import 'dart:convert';

import 'package:http/http.dart' as http;

Future<void> setAmbientLighting(String color) async {
  final response = await http.post(
    Uri.parse('http://localhost:5000/ambient/lighting'),
    headers: <String, String>{
      'Content-Type': 'application/json; charset=UTF-8',
    },
    body: jsonEncode(<String, dynamic>{ 'color': color })
  );

  print(jsonDecode(response.body)); // Handle response appropriately in your app
}

Future<void> setTemperature(int temp) async {
  final response = await http.post(
    Uri.parse('http://localhost:5000/ambient/temperature'),
    headers: <String, String>{
      'Content-Type': 'application/json; charset=UTF-8',
    },
    body: jsonEncode(<String, dynamic>{ 'temp': temp })
  );

  print(jsonDecode(response.body)); // Handle response appropriately in your app
}

Future<void> setAudioVolume(int volume) async {
  final response = await http.post(
    Uri.parse('http://localhost:5000/ambient/audio'),
    headers: <String, String>{
      'Content-Type': 'application/json; charset=UTF-8',
    },
    body: jsonEncode(<String, dynamic>{ 'volume': volume })
  );

  print(jsonDecode(response.body)); // Handle response appropriately in your app
}

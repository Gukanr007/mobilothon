import 'dart:convert';

import 'package:http/http.dart' as http;

Future<void> sendSensorData(double acceleration) async {
  final response = await http.post(
    Uri.parse('http://localhost:5000/detect-accident'),
    headers: <String, String>{
      'Content-Type': 'application/json; charset=UTF-8',
    },
    body: jsonEncode(<String, dynamic>{
      'acceleration': acceleration
    }),
  );

  if (response.statusCode == 200) {
    var jsonResponse = jsonDecode(response.body);
    if (jsonResponse['accident']) {
      print('Accident Detected: ${jsonResponse['message']}');
      // Implement actions like notifying user or emergency services here
    } else {
      print('No Accident Detected.');
    }
  } else {
    throw Exception('Failed to send sensor data.');
  }
}

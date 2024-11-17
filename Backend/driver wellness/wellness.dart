import 'dart:convert';

import 'package:http/http.dart' as http;

Future<void> sendWellnessData(int heartRate, String activityLevel) async {
  final response = await http.post(
    Uri.parse('http://localhost:5000/driver/wellness'),
    headers: <String, String>{
      'Content-Type': 'application/json; charset=UTF-8',
    },
    body: jsonEncode(<String, dynamic>{
      'heart_rate': heartRate,
      'activity_level': activityLevel
    }),
  );

  if (response.statusCode == 200) {
    var jsonResponse = jsonDecode(response.body);
    print(jsonResponse);
  } else {
    throw Exception('Failed to update wellness data.');
  }
}

import 'dart:convert';

import 'package:http/http.dart' as http;

Future<int> predictMaintenance(int mileage, int age, int averageRpm, int numberOfAlerts) async {
  final response = await http.post(
    Uri.parse('http://localhost:5000/predict-maintenance'),
    headers: <String, String>{
      'Content-Type': 'application/json; charset=UTF-8',
    },
    body: jsonEncode(<String, dynamic>{
      'mileage': mileage,
      'age': age,
      'average_rpm': averageRpm,
      'number_of_alerts': numberOfAlerts
    }),
  );

  if (response.statusCode == 200) {
    var jsonResponse = jsonDecode(response.body);
    return jsonResponse['days_until_next_maintenance'];
  } else {
    throw Exception('Failed to predict maintenance.');
  }
}

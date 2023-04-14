import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';

import '../../utils/app_theme.dart';
import '../../widgets/custom_button.dart';
import '../connect/connect_screen.dart';
import '../dashboard/dashboard_screen.dart';
import 'bloc/home_bloc.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  // @override
  // void initState() {
  //   super.initState();
  // }
  final List<Map<String, String>> _availableDevices = [
    {
      'title': 'computer 1',
      'ipAddress': '192.0.8.xx',
    },
    {
      'title': 'computer 2',
      'ipAddress': '192.0.8.xx',
    },
    {
      'title': 'computer 3',
      'ipAddress': '192.0.8.xx',
    },
    {
      'title': 'computer 1',
      'ipAddress': '192.0.8.xx',
    },
    {
      'title': 'computer 2',
      'ipAddress': '192.0.8.xx',
    },
    {
      'title': 'computer 3',
      'ipAddress': '192.0.8.xx',
    },
    {
      'title': 'computer 1',
      'ipAddress': '192.0.8.xx',
    },
    {
      'title': 'computer 2',
      'ipAddress': '192.0.8.xx',
    },
    {
      'title': 'computer 3',
      'ipAddress': '192.0.8.xx',
    },
  ];
  bool _isExpanded = false;
  // final List<bool> _isExpandedList = [false, false, false];
  @override
  void dispose() {
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    double height = MediaQuery.of(context).size.height;
    double width = MediaQuery.of(context).size.width;
    final padding = MediaQuery.of(context).viewPadding;
    height = height - padding.top - padding.bottom;
    return BlocConsumer<HomeScreenBloc, HomeScreenState>(
      listener: (context, state) {
        // TODO: implement listener
      },
      builder: (context, state) {
        if (state is HomeInitial) {
          return Scaffold(
            appBar: AppBar(
              title: const Text('Tech-Shila'),
              centerTitle: true,
            ),
            body: SingleChildScrollView(
              child: SizedBox(
                height: height,
                width: width,
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.start,
                  children: [
                    CustomButton(
                      height: height * 0.08,
                      onPressed: () {},
                      width: width * 0.4,
                      buttonText: 'Available Devices',
                      margin: EdgeInsets.symmetric(
                        vertical: height * 0.05,
                      ),
                    ),
                    SingleChildScrollView(
                      child: SizedBox(
                        height: _isExpanded ? height * 0.65 : height * 0.45,
                        width: width * 0.4,
                        child: Column(
                          children: [
                            Expanded(
                              child: SizedBox(
                                width: width * 0.4,
                                child: ListView.builder(
                                  shrinkWrap: true,
                                  scrollDirection: Axis.vertical,
                                  itemCount: _isExpanded
                                      ? _availableDevices.length
                                      : 2,
                                  itemBuilder:
                                      (BuildContext context, int index) {
                                    return Container(
                                      height: height * 0.1,
                                      color: AppTheme.borderColor,
                                      margin: EdgeInsets.symmetric(
                                          vertical: height * 0.01),
                                      child: ListTile(
                                        onTap: () {
                                          Navigator.push(
                                              context,
                                              MaterialPageRoute(
                                                  builder: (context) =>
                                                      const DashboardScreen()));
                                        },
                                        title: Text(
                                            _availableDevices[index]['title']!),
                                        subtitle: Text(_availableDevices[index]
                                            ['ipAddress']!),
                                      ),
                                    );
                                  },
                                ),
                              ),
                            ),
                            CustomButton(
                              height: height * 0.08,
                              width: width * 0.4,
                              margin: EdgeInsets.symmetric(
                                vertical: height * 0.05,
                              ),
                              onPressed: () {
                                setState(() {
                                  _isExpanded = !_isExpanded;
                                });
                              },
                              buttonText:
                                  _isExpanded ? 'Show Less' : 'Show more',
                            ),
                          ],
                        ),
                      ),
                    ),
                    Column(
                      mainAxisAlignment: MainAxisAlignment.start,
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        TextButton(
                          onPressed: () {},
                          child: const Text(
                            'New Device?',
                            style: TextStyle(
                                color: AppTheme.blackColor,
                                decoration: TextDecoration.underline),
                          ),
                        ),
                        CustomButton(
                          height: height * 0.08,
                          width: width * 0.8,
                          onPressed: () {
                            Navigator.push(
                              context,
                              MaterialPageRoute(
                                builder: (context) => ConnectScreen(),
                              ),
                            );
                          },
                          buttonText: 'Connect to new device',
                        ),
                      ],
                    ),
                  ],
                ),
              ),
            ),
          );
        }
        return const Scaffold(
          body: Center(
            child: CircularProgressIndicator(),
          ),
        );
      },
    );
  }
}

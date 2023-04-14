import 'package:fluent_ui/fluent_ui.dart';
import 'package:techshila_pc_client/utils/app_theme.dart';
import 'package:techshila_pc_client/utils/splash_screen.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return FluentApp(
      debugShowCheckedModeBanner: false,
      title: 'Tech-Shila',
      theme: FluentThemeData.light().copyWith(
        scaffoldBackgroundColor: AppTheme.whiteColor,
        typography: const Typography.raw(
          title:
              TextStyle(fontFamily: 'Cera Pro', color: AppTheme.mainFontColor),
          body:
              TextStyle(fontFamily: 'Cera Pro', color: AppTheme.mainFontColor),
          bodyLarge:
              TextStyle(fontFamily: 'Cera Pro', color: AppTheme.mainFontColor),
          bodyStrong:
              TextStyle(fontFamily: 'Cera Pro', color: AppTheme.mainFontColor),
          caption:
              TextStyle(fontFamily: 'Cera Pro', color: AppTheme.mainFontColor),
          display:
              TextStyle(fontFamily: 'Cera Pro', color: AppTheme.mainFontColor),
          subtitle:
              TextStyle(fontFamily: 'Cera Pro', color: AppTheme.mainFontColor),
          titleLarge:
              TextStyle(fontFamily: 'Cera Pro', color: AppTheme.mainFontColor),
        ),
        shadowColor: AppTheme.borderColor,
        acrylicBackgroundColor: AppTheme.whiteColor,
        focusTheme: FocusThemeData(
          glowColor: AppTheme.mainFontColor,
          borderRadius: BorderRadius.circular(15),
        ),
      ),
      home: const SplashScreen(),
    );
  }
}

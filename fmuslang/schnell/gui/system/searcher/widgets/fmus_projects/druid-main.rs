use druid::widget::{Button, Flex, Label};
use druid::{AppLauncher, LocalizedString, Widget, WidgetExt, WindowDesc};

fn main() {
    // Create a window description
    let main_window = WindowDesc::new(build_ui)
        .title(LocalizedString::new("Hello, Druid!"));

    // Launch the application
    AppLauncher::with_window(main_window)
        .use_simple_logger()
        .launch("Hello, Druid!");
}

fn build_ui() -> impl Widget<()> {
    Flex::column()
        .with_child(Label::new("Welcome to Druid!"))
        .with_spacer(20.0)
        .with_child(Button::new("Click me").on_click(|_, _, _| {
            println!("Button clicked!");
        }))
}

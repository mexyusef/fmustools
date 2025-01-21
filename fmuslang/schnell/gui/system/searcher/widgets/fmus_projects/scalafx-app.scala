import scalafx.application.JFXApp
import scalafx.scene.Scene
import scalafx.scene.control.Label

object MyScalaFXApp extends JFXApp {
  stage = new JFXApp.PrimaryStage {
    title.value = "My ScalaFX App"
    scene = new Scene {
      content = new Label("Hello, ScalaFX!")
    }
  }
}

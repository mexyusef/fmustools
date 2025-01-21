import android.app.Activity
import android.os.Bundle
import android.widget.TextView

class MainActivity : Activity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        
        // Create a TextView dynamically
        val textView = TextView(this)
        textView.text = "Hello, Kotlin!"
        
        // Set the TextView as the content view for the activity
        setContentView(textView)
    }
}

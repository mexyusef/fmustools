using System;
using System.Windows.Forms;
public class MainWindow : Form
{
    public MainWindow()
    {
        this.Text = "My GUI App";

        // Add a button
        Button myButton = new Button();
        myButton.Text = "Click Me";
        myButton.Click += MyButton_Click;
        this.Controls.Add(myButton);
    }

    private void MyButton_Click(object sender, EventArgs e)
    {
        MessageBox.Show("Button Clicked!");
    }
}

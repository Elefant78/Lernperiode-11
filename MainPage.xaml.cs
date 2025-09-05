namespace RaiseMyBrainrot;

public partial class MainPage : ContentPage
{
    public MainPage()
    {
        InitializeComponent();
    }

    // Entertainment
    private void OnPlayClicked(object sender, EventArgs e)
    {
        EntertainmentBar.Progress = Math.Min(1.0, EntertainmentBar.Progress + 0.1);
    }

    // Social
    private void OnChatClicked(object sender, EventArgs e)
    {
        SocialBar.Progress = Math.Min(1.0, SocialBar.Progress + 0.1);
    }

    // Knowledge
    private void OnLearnClicked(object sender, EventArgs e)
    {
        KnowledgeBar.Progress = Math.Min(1.0, KnowledgeBar.Progress + 0.1);
    }

    // Energy
    private void OnEnergyClicked(object sender, EventArgs e)
    {
        EnergyBar.Progress = Math.Min(1.0, EnergyBar.Progress + 0.1);
    }

    // Sleep
    private void OnSleepClicked(object sender, EventArgs e)
    {
        SleepBar.Progress = Math.Min(1.0, SleepBar.Progress + 0.1);
    }
}

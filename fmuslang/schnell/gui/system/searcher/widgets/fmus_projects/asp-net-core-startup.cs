// Step 9: Update the Startup.cs file
// Open the "Startup.cs" file and update the ConfigureServices method to include the necessary services for Entity Framework Core. Add the following code inside the method:

services.AddDbContext<AppDbContext>(options =>
    options.UseSqlite(Configuration.GetConnectionString("DefaultConnection")));

// Also, update the Configure method to include routing for the TodoController. Add the following code inside the method:

app.UseRouting();
app.UseEndpoints(endpoints =>
{
    endpoints.MapControllers();
});

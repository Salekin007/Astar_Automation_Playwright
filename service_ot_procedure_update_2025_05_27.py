from playwright.sync_api import Playwright, sync_playwright, TimeoutError
# Playwright and sync_playwright are imported to enable browser automation using the synchronous API.

# TimeoutError is imported to handle exceptions when elements are not found within a given time frame.
# Define services manually
services = [
    {"Service Name": "Abscess", "OT": 1, "Procedure": 0},
    {"Service Name": "SPC", "OT": 1, "Procedure": 1},
    {"Service Name": "TURP, TURBT, BNI, Cystolitholapaxy, Ureterocele Incision, URS & ICPL, URS & Proceed", "OT": 1, "Procedure": 1}
]
# This is a list of dictionaries. Each dictionary represents a medical service.
# Each service has:
# "Service Name": Name of the service
# "OT": Whether it's an OT-related service (1 = Yes)
# "Procedure": Whether it's marked as a procedure (1 = Yes)

def run(playwright: Playwright) -> None:
# The function takes the Playwright instance and performs the entire automation flow.
    browser = playwright.chromium.launch(headless=False) #Launches Chromium browser with a visible UI (headless=False)
    context = browser.new_context()  #Creates a new browser context (like a fresh user profile)
    page = context.new_page()   #Opens a new browser tab (page)

    # Login
    page.goto("http://103.149.75.198/login")
    page.get_by_placeholder("Username").fill("admin")
    page.get_by_placeholder("Password").fill("123456")
    page.get_by_placeholder("Password").press("Enter")
    page.wait_for_timeout(2000)  #Waits for 2 seconds to allow the page to load

    # Navigate to Services Setup
    page.locator("a").filter(has_text="Administration").click()
    page.locator("a").filter(has_text="Settings").click()
    page.get_by_role("link", name=" Services Setup").click()   #Clicks through menu options: Administration → Settings → Services Setup
    page.wait_for_timeout(2000)   #Waits for 2 seconds to allow the Services Setup page to load

    not_found_services = []   #Initializes an empty list to store services that couldn't be found

    for service in services:     #Iterates over each service from the services list
        name = service["Service Name"]
        is_ot = bool(service["OT"])
        is_procedure = bool(service["Procedure"])      #Extracts and converts OT and Procedure to Boolean values (True or False)

        print(f"Updating: {name}, OT: {is_ot}, Procedure: {is_procedure}")   #Displays which service is currently being updated

        # Search service
        page.get_by_label("Search:").fill(name)     #Enters the service name in the search bar to locate it in the list
        page.wait_for_timeout(1000)      #Waits 1 second for search results to load

        try:
            # Try to click on the service row
            page.get_by_role("cell", name=name, exact=True).click()
        except TimeoutError:
            print(f"❌ Service not found: {name}")
            not_found_services.append(name)
            continue  # skip to the next service
        #Tries to click the row matching the exact service name
        # If not found, logs the name and moves to the next service
        # Click edit
        page.get_by_role("button", name=" Edit").click()
        #Clicks the Edit button for the selected service
        # Checkbox update
        checkbox_proc = page.get_by_label("Is Procedure?")
        checkbox_ot = page.get_by_label("Is OT?", exact=True)
        #Gets the "Is Procedure?" and "Is OT?" checkboxes using their label text
        # Ensure values are set correctly
        if checkbox_proc.is_checked() != is_procedure:
            checkbox_proc.check() if is_procedure else checkbox_proc.uncheck()
        if checkbox_ot.is_checked() != is_ot:
            checkbox_ot.check() if is_ot else checkbox_ot.uncheck()
        #Checks/unchecks each box only if its current state is different from the desired state

        # Submit update
        page.get_by_role("button", name="Update").click()   #Clicks the Update button to save the changes
        page.wait_for_timeout(1000)    #Waits 1 second for the operation to complete

    # Print any not found services
    if not_found_services:
        print("\n🚫 The following services were NOT found:")
        for nf in not_found_services:
            print(f" - {nf}")
    else:
        print("\n✅ All services updated successfully.")
#If any services were missing, it prints them
#Otherwise, confirms all were updated successfully

    context.close()
    browser.close()
#Closes the browser context and the browser itself to clean up


with sync_playwright() as playwright:
    run(playwright)
#This is the standard way to launch Playwright synchronously
#Passes the instance into the run() function
"""This script:

Logs into a medical web system

Navigates to the service management section

Searches for services

Updates their OT/Procedure flags

Tracks and reports any services not found in the system"""


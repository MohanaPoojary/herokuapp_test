from playwright.sync_api import sync_playwright, expect

def test_form():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://formy-project.herokuapp.com/form")
        
        heading_text=page.locator("h1").text_content()
        assert heading_text == "Complete Web Form"
        print("Heading verified successfully")
        
        # or
        # heading_text=page.locator("h1")
        # expect(heading).to_have_text("Complete Web Form")

        # fill the first name, last name, job title by using css selector
        first_name_heading=page.locator("label:has-text('First name')")
        expect(first_name_heading).to_have_text("First name")
        page.fill("#first-name", "Mohan")

        last_name_heading=page.locator("label:has-text('Last name')")
        expect(last_name_heading).to_have_text("Last name")
        page.fill("#last-name", "Poojary")

        job_title_heading=page.locator("label:has-text('Job title')")
        expect(job_title_heading).to_have_text("Job title")
        page.fill("#job-title", "Engineer")

        radio_button_text = page.locator("label:has-text('Highest level of education')")
        expect(radio_button_text).to_have_text("Highest level of education")
        print("radio_button_heading has text Highest level of education")

        # click on radio button
        page.click("#radio-button-3")
        
        # checkbox_heading=page.locator("label:has-text('Sex')")
        # expect(job_title_heading).to_have_text("Sex")

        #click on checkbox
        page.click("#checkbox-1")

        dropdown_heading=page.locator("label:has-text('Years of experience:')")
        expect(job_title_heading).to_have_text("Years of experience:")

        #select dropdown
        select_option = page.locator("#education option[selected]")
        expect(select_option).to_have_text("Select an option")
        print("Dropdown has the default 'Select an option' text")
        page.select_option("#select-menu", value="2")
        print("Dropdown option selected by value.")


        page.wait_for_timeout(2000)

test_form()
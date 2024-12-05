from playwright.sync_api import sync_playwright, expect

def test_form():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://formy-project.herokuapp.com/form")
        
        # Verify heading text
        form_heading=page.locator("h1")
        expect(form_heading).to_have_text("Complete Web Form")
        print("Heading verified successfully")
        
        # Verify label for first name input
        first_name_heading=page.locator("label[for='first-name']")
        expect(first_name_heading).to_have_text("First name")

        # Verify placeholder text in first name input field
        first_name_input_id=page.locator("#first-name")
        placeholder_text=first_name_input_id.get_attribute("placeholder")
        assert placeholder_text=="Enter first name", f"expected placeholder 'Enter first name', but got '{placeholder_text}'"
        print("Placeholder verified successfully")

        # fill input name
        first_name_input_id.fill("Mohan")
        print("First name filled successfully")

        # Verify label for last name input
        last_name_heading=page.locator("label[for='last-name']")
        expect(last_name_heading).to_have_text("Last name")

        # Verify placeholder text in last name input field
        last_name_input_id=page.locator("#last-name")
        placeholder_text=last_name_input_id.get_attribute("placeholder")
        assert placeholder_text=="Enter last name", f"expected placeholder 'Enter last name', but got '{placeholder_text}'"
        print("Placeholder verified successfully")

        # fill input name
        last_name_input_id.fill("Poojary")
        print("Last name filled successfully")

        job_title_text=page.locator("label[for='job-title']")
        expect(job_title_text).to_have_text("Job title")
        print("Job title text verified successfully")

        job_title_id=page.locator("#job-title")
        placeholder_text=job_title_id.get_attribute("placeholder")
        assert placeholder_text=="Enter your job title", f"got the job title '{placeholder_text}', instead of 'Enter your job title'"

        job_title_id.fill("Engineer")
        print("JOb title filled successfully")

        # radio-button
        radio_button=page.locator("#radio-button-1").click()
        print("Radio button clicked successfully")

        # checkbox
        checkbox=page.locator("#checkbox-1").click()
        print("Checkbox clicked successfully")

        year_of_exp_label_text=page.locator("label[for='select-menu']")
        expect(year_of_exp_label_text).to_have_text("Years of experience:")

         # Locate the dropdown
        options = page.locator("#select-menu")
        option_texts=options.all_text_contents().strip()

        print("Dropdown options:", option_texts)

        expected_options= ["Select an option", "0-1", "2-4", "5-9", "10+"]
        assert option_texts == expected_options, f"Expected {expected_options}, but got {option_texts}"

test_form()        
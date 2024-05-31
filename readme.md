# BetterCSV - A customizable and fast CSV to HTML converter.

## How do I customize my settings ?
* **Step 1:** Create a new control structure (see below in docs) using the syntax `structureName:{}` in `pref.txt`.
* **Step 2:** Inside the curly brackets of the command structure, overwrite the desired customization fields using the options given below.

### Currently Supported Customization Fields:
* **top_row_color:** Sets the background color for the top (first row) row of the table.
* **top_column_color:** Sets the background color for the cells in the top column (first column) of the table.
* **alt_color_1:** Sets the background color for alternating rows (starting from the second row).
* **alt_color_2:** Sets the background color for alternating rows (starting from the third row).
* **background_color:** Sets the background color for the surrounding HTML page.
* **cell_font_name:** Sets the font family for all cells in the table.
* **border_thickness:** Sets the thickness of the cell borders in the table.
* **border_color:** Sets the color of the cell borders in the table.
* **title_text:** Sets the text of the title displayed above the table.
* **title_color:** Sets the color of the title text.
* **switcher_font:** Sets the font of the switcher text.
* **switcher_color:** Sets the color of the switcher text.
* **switcher_font_size:** Sets the font size of the switcher text

### Currently Supported Customization Flags:
* **anti_alternating:** If set to `true`, swaps the alternating row colors.
* **title:** If set to `true`, a title is added above the table.
* **switcher:** If set to `true`, a "color-switching" dropdown list is added below, allowing for fast color-switching. Optimal for websites open to the public.
* **row_alternating:** If set to `true`, alternates the colors for rows.
* **column_alternating:** If set to `true`, alternates the colors for columns.

## Currently Supported Control Structure Options - 
General syntax is given as follows (doesn't apply to unspecified category)-
```
(control_structure_name):{
    // insert code here
}
```
* **default:** Default settings. A basic fall through in case user customization is faulty.
* **user:** User specified settings. Takes preference (higher in hierarchy relative to default) over default.
* **unspecified:** Declared differently than the other settings. Highest in hierarchy so that buggy code wouldn't derail the whole preference engine. Syntax- 
```
// code goes here- no need to declare any specific control structure.
```

## Supported Colorthemes:
*Note- check/edit colorthemes.txt to add/remove/edit custom colorthemes.*

## Alpha (currently buggy or straight-up unstable features):

*Note- Bug reports for anything relating to this category are welcome, but will probably not be fixed anytime soon. Nothing here is there to stay and is expected to be unstable in production.*

* **Cell Specific Sub-control Structure** - Use this to specify cell specific settings according to the syntax - 
``` 
parent_control_structure_name:{
    cell_specific(row_number)(column_number):{
        // code goes here
    }
}
```

## Planned features (features under consideration/review):

*Note- these features are planned or under review. There is no guarentee of them being added. If you have an implementation of any of these features that does not interfere with existing code and isn't buggy- submit a pull request.*

* **css_injection_control_structure** - Control structure allowing for css injections in parts of code.
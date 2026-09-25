// Copyright 2005 (c) The American National Corpus.  All rights reserverd.
// Permission is granted to redistribute this file, in modified or unmodified form, as
// long as the above copyright notice and this permission statement are included.
// Author: Keith Suderman (suderman@cs.vassar.edu)

// Used to look for whitespace in form data.
var whitespace = ' \t\n\r';

// These are the subdomains to use on the upload page. The values in the subdomain combo box
// depend on the domain that is selected.
var subdomains = [
   ["Select a sub-domain"],
   ["Select a sub-domain", "Engineering", "Communications", "Technology", "Computing", "Energy", "Transport"],
   ["Select a sub-domain", "Visual Arts", "Architecture", "Performing", "Media", "Literary", "Design"],
   ["Select a sub-domain", "Religion", "Philosophy", "Occult", "Mythology", "Folklore"],
   ["Select a sub-domain", "Business", "Finance", "Industry", "Employment", "Occupations"],
   ["Select a sub-domain", "Food", "Travel", "Fashion", "Sport", "Household", "Antiques", "Hobbies", "Gardening"],
   ["Select a sub-domain", "Math", "Physics", "Chemistry", "Biology", "Astronomy"],
   ["Select a sub-domain", "Sociology",  "Geography", "Anthropology", "Medicine", "Psychiatry", "Psychology", "Law", "Education", "Linguistics"],
   ["Select a sub-domain", "History", "Government", "Politics", "Military", "Archaeology", "Economics", "Development"]
];


function selectSubdomain()
{
	// The the two combo boxes.
	//var domain = document.getElementById("select-domain");
	//var subdomain = document.getElementById("select-subdomain");
	var domain = get('select-domain');
	var subdomain = get('select-subdomain');
	// Get the index of the currently selected domain, and use the
	// index to get the list of appropriate subdomains.
	var index = domain.selectedIndex;
	var choices = subdomains[index];
	// Update the subdomain combo box.  We need to empty it first (set the length to zero)
	// and then re-populate it.
	subdomain.options.length = 0;
	for (i = 0; i < choices.length; ++i)
	{
		subdomain.options[subdomain.options.length] = new Option(choices[i]);
	}
}

function enable(id)
{
	var control = get(id);
	control.disabled = false;
}

function disable(id)
{
	var control = get(id);
	control.disabled = true;
}

function uncheck(id)
{
	var control = get(id);
	control.checked = false;
}

function non_fiction()
{
	enable("select-domain");
	enable("select-subdomain");
	disable("select-fiction");
	uncheck("radio-fiction");
}

function fiction()
{
	uncheck("radio-non-fiction");
	disable("select-domain");
	disable("select-subdomain");
	enable("select-fiction");
}

// These should be moved out of menu.js
function isEmpty(s)
{
	if (s == null || s.length == 0)
	{
		return true;
	}
	
	var i;
	for (i = 0; i < s.length; ++i)
	{
		var c = s.charAt(i);
		if (whitespace.indexOf(c) == -1)
		{
			return false;
		}
	}
	return true;
}

function checkValue(control, message)
{
	var e = get(control);
	if (e.selectedIndex == 0)
	{	
		alert(message);
		//control.focus();
		return false
	}
	return true;
}

function checkText(control, message)
{
	var e = get(control);
	if (isEmpty(e.value))
	{
		alert(message);
		//control.focus();
		return false;
	}
	return true;
}

function validateForm()
{
	var radio = get('radio-fiction');
	
	if (!checkText('fname', 'No first name given.'))
		return false;
		
	if (!checkText('lname', 'The last name field can not be empty.'))
		return false;
		
	//if (!checkValue('select-region', 'No region selected.'))
	//	return false;
	
	if (radio.checked)
	{
		if (!checkValue('select-fiction', 'No genre specified.'))
			return false;
	}
	else
	{
	
		if (!checkValue('select-domain', 'No domain selected.'))
			return false;

		if (!checkValue('select-subdomain', 'No subdomain selected.'))
			return false;
	}
	if (!checkText('title', 'The title of the document must be given.'))
		return false;
		
	if (!checkText('subject', 'The subject of the document must be given.'))
		return false;
		
	return true;
}


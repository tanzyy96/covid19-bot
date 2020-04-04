
def format_in_markdown(title, articles):
    string = "```\n<< {} >>```\n".format(
        title.upper())
    i = 1
    for i in range(1, 11):
        name = articles[i]["title"]
        url = articles[i]["url"]
        source = articles[i]["source"]["name"]
        string += "{}. [{}]({})```\n|| {} ||```\n\n".format(i,
                                                            name, url, source)
    #string += "```"
    print(string)
    return string


def format_stats(data):
    try:
        country = data["country"]
        totalCases = data["cases"]
        todayCases = data["todayCases"]
        totalDeaths = data["deaths"]
        todayDeaths = data["todayDeaths"]
        totalRecovered = data["recovered"]
        casesPerMillion = data["casesPerOneMillion"]
        deathsPerMillion = data["deathsPerOneMillion"]

        string = "{} {}\n\n".format(get_flag_emoji(country), country.upper())
        string += "😷 Total Cases: {}\n".format(totalCases)
        string += "🤒 Today Cases: {}\n".format(todayCases)
        string += "☠️ Total Deaths: {}\n".format(totalDeaths)
        string += "😵 Today Deaths: {}\n".format(todayDeaths)
        string += "🤗 Total Recovered: {}\n".format(totalRecovered)
        string += "📈 Cases Per Million Citizens: {}\n".format(casesPerMillion)
        string += "📉 Deaths Per Million Citizens: {}\n".format(
            deathsPerMillion)
        return string
    except:
        return data["message"]


def get_flag_emoji(country):
    flags = {
        "🇦🇨": "Ascension Island",
        "🇦🇩": "Andorra",
        "🇦🇪": "United Arab Emirates",
        "🇦🇫": "Afghanistan",
        "🇦🇬": "Antigua & Barbuda",
        "🇦🇮": "Anguilla",
        "🇦🇱": "Albania",
        "🇦🇲": "Armenia",
        "🇦🇴": "Angola",
        "🇦🇶": "Antarctica",
        "🇦🇷": "Argentina",
        "🇦🇸": "American Samoa",
        "🇦🇹": "Austria",
        "🇦🇺": "Australia",
        "🇦🇼": "Aruba",
        "🇦🇽": "Åland Islands",
        "🇦🇿": "Azerbaijan",
        "🇧🇦": "Bosnia & Herzegovina",
        "🇧🇧": "Barbados",
        "🇧🇩": "Bangladesh",
        "🇧🇪": "Belgium",
        "🇧🇫": "Burkina Faso",
        "🇧🇬": "Bulgaria",
        "🇧🇭": "Bahrain",
        "🇧🇮": "Burundi",
        "🇧🇯": "Benin",
        "🇧🇱": "St. Barthélemy",
        "🇧🇲": "Bermuda",
        "🇧🇳": "Brunei",
        "🇧🇴": "Bolivia",
        "🇧🇶": "Caribbean Netherlands",
        "🇧🇷": "Brazil",
        "🇧🇸": "Bahamas",
        "🇧🇹": "Bhutan",
        "🇧🇻": "Bouvet Island",
        "🇧🇼": "Botswana",
        "🇧🇾": "Belarus",
        "🇧🇿": "Belize",
        "🇨🇦": "Canada",
        "🇨🇨": "Cocos (Keeling) Islands",
        "🇨🇩": "Congo - Kinshasa",
        "🇨🇫": "Central African Republic",
        "🇨🇬": "Congo - Brazzaville",
        "🇨🇭": "Switzerland",
        "🇨🇮": "Côte d’Ivoire",
        "🇨🇰": "Cook Islands",
        "🇨🇱": "Chile",
        "🇨🇲": "Cameroon",
        "🇨🇳": "China",
        "🇨🇴": "Colombia",
        "🇨🇵": "Clipperton Island",
        "🇨🇷": "Costa Rica",
        "🇨🇺": "Cuba",
        "🇨🇻": "Cape Verde",
        "🇨🇼": "Curaçao",
        "🇨🇽": "Christmas Island",
        "🇨🇾": "Cyprus",
        "🇨🇿": "Czechia",
        "🇩🇪": "Germany",
        "🇩🇬": "Diego Garcia",
        "🇩🇯": "Djibouti",
        "🇩🇰": "Denmark",
        "🇩🇲": "Dominica",
        "🇩🇴": "Dominican Republic",
        "🇩🇿": "Algeria",
        "🇪🇦": "Ceuta & Melilla",
        "🇪🇨": "Ecuador",
        "🇪🇪": "Estonia",
        "🇪🇬": "Egypt",
        "🇪🇭": "Western Sahara",
        "🇪🇷": "Eritrea",
        "🇪🇸": "Spain",
        "🇪🇹": "Ethiopia",
        "🇪🇺": "European Union",
        "🇫🇮": "Finland",
        "🇫🇯": "Fiji",
        "🇫🇰": "Falkland Islands",
        "🇫🇲": "Micronesia",
        "🇫🇴": "Faroe Islands",
        "🇫🇷": "France",
        "🇬🇦": "Gabon",
        "🇬🇧": "UK",
        "🇬🇩": "Grenada",
        "🇬🇪": "Georgia",
        "🇬🇫": "French Guiana",
        "🇬🇬": "Guernsey",
        "🇬🇭": "Ghana",
        "🇬🇮": "Gibraltar",
        "🇬🇱": "Greenland",
        "🇬🇲": "Gambia",
        "🇬🇳": "Guinea",
        "🇬🇵": "Guadeloupe",
        "🇬🇶": "Equatorial Guinea",
        "🇬🇷": "Greece",
        "🇬🇸": "South Georgia & South Sandwich Islands",
        "🇬🇹": "Guatemala",
        "🇬🇺": "Guam",
        "🇬🇼": "Guinea-Bissau",
        "🇬🇾": "Guyana",
        "🇭🇰": "Hong Kong",
        "🇭🇲": "Heard & McDonald Islands",
        "🇭🇳": "Honduras",
        "🇭🇷": "Croatia",
        "🇭🇹": "Haiti",
        "🇭🇺": "Hungary",
        "🇮🇨": "Canary Islands",
        "🇮🇩": "Indonesia",
        "🇮🇪": "Ireland",
        "🇮🇱": "Israel",
        "🇮🇲": "Isle of Man",
        "🇮🇳": "India",
        "🇮🇴": "British Indian Ocean Territory",
        "🇮🇶": "Iraq",
        "🇮🇷": "Iran",
        "🇮🇸": "Iceland",
        "🇮🇹": "Italy",
        "🇯🇪": "Jersey",
        "🇯🇲": "Jamaica",
        "🇯🇴": "Jordan",
        "🇯🇵": "Japan",
        "🇰🇪": "Kenya",
        "🇰🇬": "Kyrgyzstan",
        "🇰🇭": "Cambodia",
        "🇰🇮": "Kiribati",
        "🇰🇲": "Comoros",
        "🇰🇳": "St. Kitts & Nevis",
        "🇰🇵": "North Korea",
        "🇰🇷": "South Korea",
        "🇰🇼": "Kuwait",
        "🇰🇾": "Cayman Islands",
        "🇰🇿": "Kazakhstan",
        "🇱🇦": "Laos",
        "🇱🇧": "Lebanon",
        "🇱🇨": "St. Lucia",
        "🇱🇮": "Liechtenstein",
        "🇱🇰": "Sri Lanka",
        "🇱🇷": "Liberia",
        "🇱🇸": "Lesotho",
        "🇱🇹": "Lithuania",
        "🇱🇺": "Luxembourg",
        "🇱🇻": "Latvia",
        "🇱🇾": "Libya",
        "🇲🇦": "Morocco",
        "🇲🇨": "Monaco",
        "🇲🇩": "Moldova",
        "🇲🇪": "Montenegro",
        "🇲🇫": "St. Martin",
        "🇲🇬": "Madagascar",
        "🇲🇭": "Marshall Islands",
        "🇲🇰": "North Macedonia",
        "🇲🇱": "Mali",
        "🇲🇲": "Myanmar (Burma)",
        "🇲🇳": "Mongolia",
        "🇲🇴": "Macao Sar China",
        "🇲🇵": "Northern Mariana Islands",
        "🇲🇶": "Martinique",
        "🇲🇷": "Mauritania",
        "🇲🇸": "Montserrat",
        "🇲🇹": "Malta",
        "🇲🇺": "Mauritius",
        "🇲🇻": "Maldives",
        "🇲🇼": "Malawi",
        "🇲🇽": "Mexico",
        "🇲🇾": "Malaysia",
        "🇲🇿": "Mozambique",
        "🇳🇦": "Namibia",
        "🇳🇨": "New Caledonia",
        "🇳🇪": "Niger",
        "🇳🇫": "Norfolk Island",
        "🇳🇬": "Nigeria",
        "🇳🇮": "Nicaragua",
        "🇳🇱": "Netherlands",
        "🇳🇴": "Norway",
        "🇳🇵": "Nepal",
        "🇳🇷": "Nauru",
        "🇳🇺": "Niue",
        "🇳🇿": "New Zealand",
        "🇴🇲": "Oman",
        "🇵🇦": "Panama",
        "🇵🇪": "Peru",
        "🇵🇫": "French Polynesia",
        "🇵🇬": "Papua New Guinea",
        "🇵🇭": "Philippines",
        "🇵🇰": "Pakistan",
        "🇵🇱": "Poland",
        "🇵🇲": "St. Pierre & Miquelon",
        "🇵🇳": "Pitcairn Islands",
        "🇵🇷": "Puerto Rico",
        "🇵🇸": "Palestinian Territories",
        "🇵🇹": "Portugal",
        "🇵🇼": "Palau",
        "🇵🇾": "Paraguay",
        "🇶🇦": "Qatar",
        "🇷🇪": "Réunion",
        "🇷🇴": "Romania",
        "🇷🇸": "Serbia",
        "🇷🇺": "Russia",
        "🇷🇼": "Rwanda",
        "🇸🇦": "Saudi Arabia",
        "🇸🇧": "Solomon Islands",
        "🇸🇨": "Seychelles",
        "🇸🇩": "Sudan",
        "🇸🇪": "Sweden",
        "🇸🇬": "Singapore",
        "🇸🇭": "St. Helena",
        "🇸🇮": "Slovenia",
        "🇸🇯": "Svalbard & Jan Mayen",
        "🇸🇰": "Slovakia",
        "🇸🇱": "Sierra Leone",
        "🇸🇲": "San Marino",
        "🇸🇳": "Senegal",
        "🇸🇴": "Somalia",
        "🇸🇷": "Suriname",
        "🇸🇸": "South Sudan",
        "🇸🇹": "São Tomé & Príncipe",
        "🇸🇻": "El Salvador",
        "🇸🇽": "Sint Maarten",
        "🇸🇾": "Syria",
        "🇸🇿": "Eswatini",
        "🇹🇦": "Tristan Da Cunha",
        "🇹🇨": "Turks & Caicos Islands",
        "🇹🇩": "Chad",
        "🇹🇫": "French Southern Territories",
        "🇹🇬": "Togo",
        "🇹🇭": "Thailand",
        "🇹🇯": "Tajikistan",
        "🇹🇰": "Tokelau",
        "🇹🇱": "Timor-Leste",
        "🇹🇲": "Turkmenistan",
        "🇹🇳": "Tunisia",
        "🇹🇴": "Tonga",
        "🇹🇷": "Turkey",
        "🇹🇹": "Trinidad & Tobago",
        "🇹🇻": "Tuvalu",
        "🇹🇼": "Taiwan",
        "🇹🇿": "Tanzania",
        "🇺🇦": "Ukraine",
        "🇺🇬": "Uganda",
        "🇺🇲": "U.S. Outlying Islands",
        "🇺🇳": "United Nations",
        "🇺🇸": "USA",
        "🇺🇾": "Uruguay",
        "🇺🇿": "Uzbekistan",
        "🇻🇦": "Vatican City",
        "🇻🇨": "St. Vincent & Grenadines",
        "🇻🇪": "Venezuela",
        "🇻🇬": "British Virgin Islands",
        "🇻🇮": "U.S. Virgin Islands",
        "🇻🇳": "Vietnam",
        "🇻🇺": "Vanuatu",
        "🇼🇫": "Wallis & Futuna",
        "🇼🇸": "Samoa",
        "🇽🇰": "Kosovo",
        "🇾🇪": "Yemen",
        "🇾🇹": "Mayotte",
        "🇿🇦": "South Africa",
        "🇿🇲": "Zambia",
        "🇿🇼": "Zimbabwe",
        "🏴󠁧󠁢󠁥󠁮󠁧󠁿": "England",
        "🏴󠁧󠁢󠁳󠁣󠁴󠁿": "Scotland",
        "🏴󠁧󠁢󠁷󠁬󠁳󠁿": "Wales"
    }
    for key, value in flags.items():
        if value.lower() == country.lower():
            return key
    return ""

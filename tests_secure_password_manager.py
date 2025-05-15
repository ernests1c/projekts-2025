from cryptography.fernet import Fernet
from secure_password_manager import (
    add_password, get_password, generate_key
)

def test_encryption_decryption(tmp_path, monkeypatch):
    test_file = tmp_path / "passwords.json"
    monkeypatch.setattr("secure_password_manager.DATA_FILE", str(test_file))

    key = generate_key("testmaster")
    fernet = Fernet(key)

    add_password("mytest", "tester", "pass123", fernet)
    result = get_password("mytest", fernet)

    assert result["username"] == "tester"
    assert result["password"] == "pass123"


###
# ja lietotājs ievada savu masterparoli, tā tiek saglabāta un var tālāk ievadīt datus
# ja lietotājs vēlās iziet ārā no programmas, tad uzspiež 3 un var beigt darbību ar programmu

# ja lietotājs ievada nepareizo masterparoli, tiek parādīts kļūdas ziņojums, un programma nepieļauj piekļuvi
#ja lietotājs mēģina pievienot ierakstu ar jau esošu nosaukumu, ieraksts tiek pārrakstīts
# ja lietotājs pievieno vairākus ierakstus pēc kārtas, visi tiek pareizi nolasīti un atšifrēti
# ja lietotājs aizver programmu pēc saglabāšanas, visi dati joprojām ir pieejami - parole tiek pareizi nolasīta no JSON

#ja lietotājs atstāj vienu vai vairākus laukus tukšus, programma nepieļauj ieraksta saglabāšanu un parāda kļūdu
#ja lietotājs ievada paroli ar ļoti daudz simboliem, programma vēljoprojām to apstrādā.

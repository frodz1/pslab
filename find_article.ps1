param (
    [string]$Temat,
    [string]$Jezyk,
    [int]$Limit,
    [string]$ApiKey
)

function Wyszukaj-Artykuly-NewsData {
    param (
        [string]$Temat,
        [string]$Jezyk,
        [int]$Limit,
        [string]$Key
    )

    $encodedQuery = [uri]::EscapeDataString($Temat)
    $url = "https://newsdata.io/api/1/news?apikey=$Key&q=$encodedQuery&language=$Jezyk"

    try {
        $response = Invoke-RestMethod -Uri "https://newsdata.io/api/1/news?apikey=$Key&q=$encodedQuery&language=$Jezyk" -Method Get

        if ($response.status -eq "success") {
            $articles = $response.results | Select-Object -First $Limit

            if ($articles.Count -eq 0) {
                Write-Output "Brak wyników dla zapytania '$Temat'."
            } else {
                Write-Output "`nWyniki wyszukiwania dla tematu: '$Temat'`n"
                foreach ($article in $articles) {
                    Write-Output "$($article.title)"
                    Write-Output " Data: $($article.pubDate)"
                    Write-Output " Link: $($article.link)`n"
                }
            }
        } else {
            Write-Error "Błąd API: $($response.message)"
        }
    } catch {
        Write-Error "Błąd podczas wywołania API"
    }
}

# Uruchomienie funkcji z parametrami skryptu
Wyszukaj-Artykuly-NewsData -Temat $Temat -Jezyk $Jezyk -Limit $Limit -Key $ApiKey

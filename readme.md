# Val Frejus Meteo - Integration Home Assistant

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)
[![GitHub release](https://img.shields.io/github/release/El-Daron/valfrejus-weather.svg)](https://github.com/El-Daron/valfrejus-weather/releases)

Integration Home Assistant pour recuperer les donnees meteo et neige de la station de ski Val Frejus via Lumiplan.

## Nouveaute v2.0

**Configuration via interface graphique !** Plus besoin de modifier `configuration.yaml`

## Donnees disponibles

L'integration cree **17 sensors** avec les donnees suivantes :

### Village (1550m)
- Temperature matin et apres-midi (°C)
- Vitesse et direction du vent
- Hauteur de neige totale (cm)
- Qualite de la neige
- Neige fraiche (cm)
- Date derniere chute de neige

### Sommet - Punta Bagna (2737m)
- Temperature matin et apres-midi (°C)
- Vitesse et direction du vent
- Hauteur de neige totale (cm)
- Qualite de la neige
- Neige fraiche (cm)
- Date derniere chute de neige

**Mise a jour automatique toutes les 6 heures**

## Installation

### Via HACS (Recommande)

1. Ouvrez HACS dans Home Assistant
2. Cliquez sur les 3 points en haut a droite
3. Selectionnez "Custom repositories"
4. Ajoutez l'URL : `https://github.com/El-Daron/valfrejus-weather`
5. Categorie : `Integration`
6. Cliquez sur "Add"
7. Recherchez "Val Frejus Meteo" et installez
8. **Redemarrez Home Assistant**

### Installation manuelle

1. Telechargez le dossier `custom_components/valfrejus_weather`
2. Copiez-le dans votre dossier `custom_components` de Home Assistant
3. Redemarrez Home Assistant

## Configuration

**Configuration via l'interface graphique**

1. Allez dans **Configuration** -> **Integrations**
2. Cliquez sur **+ Ajouter une integration**
3. Recherchez **"Val Frejus"**
4. Suivez l'assistant de configuration
5. C'est tout ! Les sensors sont automatiquement crees

**Aucune modification de `configuration.yaml` necessaire !**

## Exemple de carte Lovelace

```yaml
type: vertical-stack
cards:
  - type: markdown
    content: |
      # Val Frejus - Meteo & Neige
      
  - type: horizontal-stack
    cards:
      - type: entity
        entity: sensor.val_frejus_village_temperature_matin
        name: Village Matin
        icon: mdi:thermometer
      - type: entity
        entity: sensor.val_frejus_village_temperature_apres_midi
        name: Village Apres-midi
        icon: mdi:thermometer
        
  - type: horizontal-stack
    cards:
      - type: entity
        entity: sensor.val_frejus_village_hauteur_neige
        name: Neige Village
        icon: mdi:snowflake
      - type: entity
        entity: sensor.val_frejus_sommet_hauteur_neige
        name: Neige Sommet
        icon: mdi:snowflake
```

## Problemes et suggestions

Ouvrez une issue sur [GitHub](https://github.com/El-Daron/valfrejus-weather/issues)

## Licence

MIT License

## Credits

Donnees fournies par [Lumiplan](https://bulletinv3.lumiplan.pro/)

---

Si cette integration vous plait, n'hesitez pas a mettre une etoile sur GitHub !

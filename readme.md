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
  - type: custom:mushroom-title-card
    title: ⛷️ Val Frejus
    subtitle: Conditions actuelles de ski
  - square: false
    type: grid
    columns: 2
    cards:
      - type: vertical-stack
        cards:
          - type: custom:mushroom-entity-card
            entity: sensor.val_frejus_village_temperature_matin
            name: Temperature Matin
            icon: mdi:thermometer
            primary_info: state
            secondary_info: name
          - type: custom:mushroom-entity-card
            entity: sensor.val_frejus_village_temperature_apres_midi
            name: Temperature Apres-midi
            icon: mdi:thermometer
            primary_info: state
            secondary_info: name
          - type: horizontal-stack
            cards:
              - type: custom:mushroom-entity-card
                entity: sensor.val_frejus_village_hauteur_neige
                name: Neige
                icon: mdi:snowflake
                icon_color: blue
                layout: vertical
              - type: custom:mushroom-entity-card
                entity: sensor.val_frejus_village_neige_fraiche
                name: Fraiche
                icon: mdi:snowflake-alert
                icon_color: cyan
                layout: vertical
          - type: custom:mushroom-entity-card
            entity: sensor.val_frejus_village_vitesse_vent
            name: Vent
            icon: mdi:weather-windy
            secondary_info: state
            badge_icon: mdi:compass
            badge_color: grey
          - type: custom:mushroom-entity-card
            entity: sensor.val_frejus_village_qualite_neige
            name: Qualite neige
            icon: mdi:snowflake-variant
            icon_color: light-blue
        title: Village 1550m
      - type: vertical-stack
        cards:
          - type: custom:mushroom-entity-card
            entity: sensor.val_frejus_sommet_temperature_matin
            name: Temperature Matin
            icon: mdi:thermometer
            primary_info: state
            secondary_info: name
          - type: custom:mushroom-entity-card
            entity: sensor.val_frejus_sommet_temperature_apres_midi
            name: Temperature Apres-midi
            icon: mdi:thermometer
            primary_info: state
            secondary_info: name
          - type: horizontal-stack
            cards:
              - type: custom:mushroom-entity-card
                entity: sensor.val_frejus_sommet_hauteur_neige
                name: Neige
                icon: mdi:snowflake
                icon_color: blue
                layout: vertical
              - type: custom:mushroom-entity-card
                entity: sensor.val_frejus_sommet_neige_fraiche
                name: Fraiche
                icon: mdi:snowflake-alert
                icon_color: cyan
                layout: vertical
          - type: custom:mushroom-entity-card
            entity: sensor.val_frejus_sommet_vitesse_vent
            name: Vent
            icon: mdi:weather-windy
            secondary_info: state
            badge_icon: mdi:compass
            badge_color: grey
          - type: custom:mushroom-entity-card
            entity: sensor.val_frejus_sommet_qualite_neige
            name: Qualite neige
            icon: mdi:snowflake-variant
            icon_color: light-blue
        title: Sommet 2737m
  - type: custom:mini-graph-card
    name: Evolution Temperatures
    hours_to_show: 48
    points_per_hour: 0.5
    line_width: 3
    font_size: 75
    animate: true
    show:
      labels: true
      legend: true
      points: false
    entities:
      - entity: sensor.val_frejus_village_temperature_apres_midi
        name: Village
        color: "#667eea"
      - entity: sensor.val_frejus_sommet_temperature_apres_midi
        name: Sommet
        color: "#f5576c"
  - type: custom:mushroom-chips-card
    alignment: center
    chips:
      - type: weather
        entity: weather.home
        show_conditions: true
        show_temperature: true
      - type: entity
        entity: sensor.val_frejus_derniere_mise_a_jour
        icon: mdi:update
        content_info: state
        card_mod:
          style: |
            ha-card {
               background: none !important;
               box-shadow: none !important;
               color: white !important;
             }
      - type: template
        icon: mdi:refresh
        content: Actualiser
        tap_action:
          action: call-service
          service: homeassistant.update_entity
          target:
            entity_id: sensor.val_frejus_village_temperature_matin
        card_mod:
          style: |
            ha-card {
               background: none !important;
               box-shadow: none !important;
               color: white !important;
             }
  - type: custom:mushroom-title-card
    title: Informations complementaires
  - type: entities
    show_header_toggle: false
    entities:
      - entity: sensor.val_frejus_village_direction_vent
        name: Direction vent Village
        icon: mdi:compass
        secondary_info: none
      - entity: sensor.val_frejus_sommet_direction_vent
        name: Direction vent Sommet
        icon: mdi:compass
      - entity: sensor.val_frejus_village_derniere_chute
        name: Derniere chute Village
        icon: mdi:calendar-clock
      - entity: sensor.val_frejus_sommet_derniere_chute
        name: Derniere chute Sommet
        icon: mdi:calendar-clock
    state_color: false

```

## Problemes et suggestions

Ouvrez une issue sur [GitHub](https://github.com/El-Daron/valfrejus-weather/issues)

## Licence

MIT License

## Credits

Donnees fournies par [Lumiplan](https://bulletinv3.lumiplan.pro/)

---

Si cette integration vous plait, n'hesitez pas a mettre une etoile sur GitHub !

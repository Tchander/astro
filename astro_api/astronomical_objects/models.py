from django.db import models


class AstroObjectBaseModel(models.Model):
    DECIMAL_CONFIGS = {
        'max_digits': 18,
        'decimal_places': 6,
    }
    name = models.CharField("Name", max_length=100, default=None)
    object_type = models.CharField("Object type", max_length=100, default=None)
    mass_kg = models.DecimalField("Mass in kg", max_digits=50, decimal_places=8, default=None)
    radius_km = models.DecimalField("Radius in km", **DECIMAL_CONFIGS, default=None)
    density_gcm3 = models.DecimalField("Density in g/cm3", **DECIMAL_CONFIGS, default=None)
    rotation_period_days = models.DecimalField("Rotation period in days", **DECIMAL_CONFIGS, default=None)
    temperature_kelvin = models.DecimalField("Temperature in Kelvins", **DECIMAL_CONFIGS, default=None)

    class Meta:
        abstract = True


class StarObject(AstroObjectBaseModel):
    known_planets = models.PositiveSmallIntegerField("Known planets", default=None)
    type_of_star = models.CharField("Type of star", max_length=10, default=None)
    description_of_type = models.CharField("Description of star's type", max_length=50, default=None)
    age = models.DecimalField("Age of the star", max_digits=20, decimal_places=6, default=None)
    distance_to_the_sun_ly = models.DecimalField(
        "Distance to the sun in light years", max_digits=18, decimal_places=6, default=None
    )
    right_ascension_h = models.PositiveSmallIntegerField("Hours of right ascension", default=None)
    right_ascension_m = models.PositiveSmallIntegerField("Minutes of right ascension", default=None)
    right_ascension_s = models.DecimalField("Seconds of right ascension", max_digits=10, decimal_places=8, default=None)
    declination_d = models.SmallIntegerField("Degrees of declination", default=None)
    declination_m = models.PositiveSmallIntegerField("Minutes of declination", default=None)
    declination_s = models.DecimalField("Seconds of declination", max_digits=10, decimal_places=8, default=None)


class NotStarObject(AstroObjectBaseModel):
    DECIMAL_CONFIGS = {
        'max_digits': 18,
        'decimal_places': 6
    }
    known_satellites = models.PositiveSmallIntegerField("Known satellites", default=None)
    aphelion_km = models.DecimalField("Aphelion in km", **DECIMAL_CONFIGS, default=None)
    perihelion_km = models.DecimalField("Perihelion in km", **DECIMAL_CONFIGS, default=None)
    semi_major_axis_km = models.DecimalField("Semi-major axis in km", **DECIMAL_CONFIGS, default=None)
    orbital_period_days = models.DecimalField("Orbital period in days", **DECIMAL_CONFIGS, default=None)
    eccentricity = models.DecimalField("Eccentricity", max_digits=12, decimal_places=10, default=None)
    inclination = models.DecimalField("Inclination", max_digits=14, decimal_places=10, default=None)
    argument_of_perihelion = models.DecimalField(
        "Argument of perihelion", max_digits=14, decimal_places=10, default=None
    )
    longitude_of_ascending_node = models.DecimalField(
        "Longitude of ascending node", max_digits=14, decimal_places=10, default=None
    )
    mean_anomaly = models.DecimalField("Mean anomaly", max_digits=14, decimal_places=10, default=None)
    albedo = models.DecimalField("Albedo", max_digits=8, decimal_places=6, default=None)

    # orbital_star_parent = models.ForeignKey(StarObject, on_delete=models.CASCADE, default=None)
    # orbital_not_star_parent = models.ForeignKey('self', on_delete=models.CASCADE, default=None)

    orbital_parent = models.CharField("Orbital parent", max_length=50, default=None)



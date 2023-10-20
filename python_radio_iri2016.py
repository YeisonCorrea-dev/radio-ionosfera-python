# -*- coding: utf-8 -*-
"""Python_radio_irI2016.ipynb

Automatically generated by Colaboratory .

Original file is located at 
    https://colab.research.google.com/drive/1Dwn2o1BlF2EaQw2mWRAzfRKUJXBI3slL
"""

!pip install iri2016   #Instalación de la blibioteca

#Instalación de librerias
import iri2016
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from datetime import datetime, timedelta
import iri2016.profile as iri

# Definir parámetros para el perfil de densidad de electrones, temperatura y foF2
time_start_stop = (datetime(2020, 10, 9, 0, 0, 0), datetime(2020, 10, 10))
time_step = timedelta(minutes=10)
alt_km_range = (100, 500, 10.)
glat = 2.4411
glon = -76.6066

# Calcular el perfil de densidad de electrones con IRI
electron_density_profile = iri.timeprofile(time_start_stop, time_step, alt_km_range, glat, glon)

# Calcular el perfil de temperatura con IRI
temperature_profile = iri.timeprofile(time_start_stop, time_step, alt_km_range, glat, glon)

# Calcular el perfil de foF2 con IRI
foF2_profile = iri.timeprofile(time_start_stop, time_step, alt_km_range, glat, glon)

# Crear el gráfico de densidad de electrones
fig1, ax1 = plt.subplots()
date_format = DateFormatter("%H:%M")
ax1.xaxis.set_major_formatter(date_format)
pcmesh1 = ax1.pcolormesh(electron_density_profile.time, electron_density_profile.alt_km, electron_density_profile.ne.T, shading="nearest", cmap="viridis")
plt.colorbar(pcmesh1, ax=ax1, label="Densidad de Electrones (cm^-3)")
ax1.set_title("Perfil de Densidad de Electrones")
ax1.set_xlabel("Hora del Día")
ax1.set_ylabel("Altitud (km)")

# Crear el gráfico de temperatura
fig2, ax2 = plt.subplots()
ax2.xaxis.set_major_formatter(date_format)
pcmesh2 = ax2.pcolormesh(temperature_profile.time, temperature_profile.alt_km, temperature_profile.Tn.T, shading="nearest", cmap="coolwarm")
plt.colorbar(pcmesh2, ax=ax2, label="Temperatura (K)")
ax2.set_title("Perfil de Temperatura")
ax2.set_xlabel("Hora del Día")
ax2.set_ylabel("Altitud (km)")

# Crear el gráfico de foF2
fig3, ax3 = plt.subplots()
ax3.xaxis.set_major_formatter(date_format)
ax3.plot(foF2_profile.time, foF2_profile.foF2.T)
ax3.set_title("Perfil de foF2")
ax3.set_xlabel("Hora del Día")
ax3.set_ylabel("foF2 (MHz)")

# Mostrar los gráficos de manera independiente
plt.show()


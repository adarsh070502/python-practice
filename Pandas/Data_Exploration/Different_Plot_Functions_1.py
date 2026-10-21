# Create locators for ticks on the time axis
plt.figure(figsize=(14,8),dpi=120)
plt.title('Tesla Web Search vs Price', fontsize=18)

plt.xticks(rotation=45)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylim([0, 600])
ax1.set_xlim([df_tesla.MONTH.min(), df_tesla.MONTH.max()])

ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE, "#FF5733", linewidth=3)
ax2.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH, "c", linewidth=3)

ax1.set_xlabel("Time", fontsize=14)
ax1.set_ylabel("TSLA STOCK PRICE", color="#FF5733", fontsize=14)
ax2.set_ylabel("TSLA Web trend", color="c", fontsize=14)


# to get linbetween lines in xaxis
years = mdates.YearLocator()
months = mdates.MonthLocator()
years_fmt = mdates.DateFormatter("%Y")

ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)
#to get linbetween lines in xaxis

plt.show()


